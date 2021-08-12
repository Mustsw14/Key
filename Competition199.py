from _csv import _writer
from abc import ABC, abstractmethod
import pickle
import os.path
import csv
from csv import writer
from os import path
from typing import List, Any


class IdentifiedObject(ABC):

    def __init__(self, oid):
        self._oid = oid

    @abstractmethod
    def oid(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __hash__(self):
        pass


class TeamMember(IdentifiedObject):

    def __init__(self, oid, _player_name, _player_email):
        super().__init__(oid)
        self._name = _player_name
        self._email = _player_email

    @property
    def oid(self):
        return self._oid

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, prop):
        if prop is not None:
            self._name = prop

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, prop):
        if self._email is not None:
            self._email = prop

    def __str__(self):
        return str(self.name + "<" + self.email + ">")

    def __eq__(self, other):
        # if isinstance(other, TeamMember) and hasattr(other,"oid"):
        # if hasattr(other, "oid"):
        # return self.oid == other.oid
        # else:
        # return NotImplemented
        if self.oid == other.oid:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.oid)

    def send_email(self, emailer, subject, message):
        send_email = []
        send_email.append(self._email)
        emailer.send_plain_email(send_email, subject, message)


class Team(IdentifiedObject):

    def __init__(self, oid, _name):
        super().__init__(oid)
        self._name = _name
        self._members = []

    @property
    def oid(self):
        return self._oid

    @property
    def members(self):
        return self._members

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, prop):
        self._name = prop

    def add_member(self, member):
        if not self.members:
            return self._members.append(member)
        else:
            for members in self.members:
                if members.email in member.email:
                    raise DuplicateEmail
                if member not in self._members:
                    return self._members.append(member)
                else:
                    raise DuplicateOid

    def remove_member(self, member):
        # if member in self._members:
        self._members.remove(member)

    def __str__(self):
        return str("Team " + self.name + ": " + str(len(self._members)) + " members")

    def __eq__(self, other):
        if isinstance(other, Team) and hasattr(other, 'oid'):
            return self.oid == other.oid
        # if isinstance(other, Team) and hasattr(other,self._name):
        # return self._name == self._name
        if hasattr(other, 'name'):
            return self.name == other.name
        else:
            return NotImplemented

    def __hash__(self):
        return hash(self.oid)

    def send_email(self, emailer, subject, message):
        send_email = []
        for member in self._members:
            send_email.append(member.email)
        emailer.send_plain_email(send_email, subject, message)


class League(IdentifiedObject):

    def __init__(self, oid, league_name):
        super().__init__(oid)
        self._name = league_name
        self._competition = []
        self._teams = []

    @property
    def oid(self):
        return self._oid

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, prop):
        self._name = prop

    @property
    def competition(self):
        return self._competition

    @property
    def teams(self):
        return self._teams

    def add_teams(self, teams):
        '''
        if not self._teams:
            return self._teams.append(teams)
        else:
            for team in self._teams:
                if teams.name not in team.name:
                    return self._teams.append(teams)
                else:
                    raise DuplicateOid
        '''
        if teams not in self.teams:
            self.teams.append(teams)
        else:
            raise DuplicateOid(self._oid)

    def add_competition(self, competition):
        if not self.competition:
            return self._teams.append(competition)
        else:
            for competitions in self.competition:
                if competitions not in self.competition:
                    return self.competition.append(competition)
                else:
                    raise DuplicateOid

    def teams_for_member(self, member):
        test_team = []
        for team in self._teams:
            for members in team.members:
                if member == members:
                    test_team.append(team.name)
        return [x for x in test_team]

    def competitions_for_team(self, team):

        test_team = []
        for competition in self.competition:
            for teams in competition.teams_competing:
                if team == teams:
                    test_team.append(competition)
        return [x for x in test_team]

    def competitions_for_member(self, member):
        test_team = []
        for competition in self.competition:
            for teams in competition.teams_competing:
                for members in teams.members:
                    if member == members:
                        test_team.append(competition)
        return [x for x in test_team]

    """
    def teams_for_member(self, member):
        team_names = []
        for team in self.teams:
            if member in team.members:
                team_names.append(team.name)

        return ",".join(team_names)


        #  print([team for team in self.teams if member in team.members])

    def competitions_for_team(self, team):
        return [teams for teams in self.competition if team in competition.teams_competing]

    def competitions_for_member(self, member):
        member_teams = [team for team in self._teams if member in team.members]
        return [competition for competition in self.competitions if
                any(x in member_teams for x in competition.teams_competing)]
    """

    def __eq__(self, other):
        if isinstance(other, League) and hasattr(other, 'oid'):
            return self.oid == other.oid
        else:
            return NotImplemented

    def __hash__(self):
        return hash(self.oid)

    def __str__(self):
        return str(self.name + ": " + str(len(self._teams)) + " teams," + str(len(self.competition))) + ' competition'


class Competition(IdentifiedObject):
    @property
    def oid(self):
        return self._oid

    def __init__(self, oid, teams_playing, match_location, match_datetime):
        super().__init__(oid)
        self._teams_competing = teams_playing
        self._location = match_location
        self._date_time = match_datetime

    @property
    def teams_competing(self):
        return self._teams_competing

    @property
    def date_time(self):
        return self._date_time

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, prop):
        self._location = prop

    @date_time.setter
    def date_time(self, prop):
        self.date_time = prop

    def send_email(self, emailer, subject, message):
        team_members_emails = []
        for x in self.teams_competing:
            for y in x.members:
                team_members_emails.append(y)
        emailer.send_plain_email(team_members_emails, subject, message)

    def __hash__(self):
        return hash(self.oid)

    def __eq__(self, other):
        if isinstance(other, Competition) and hasattr(other, 'oid'):
            return self.oid == other.oid
        else:
            return NotImplemented

    def __str__(self):
        competing = []
        for test_case in self.teams_competing:
            competing.append(test_case.name)

        if self.date_time is None:
            # return str("Competition at " + self._location + " with " + ",".join(competing) + " teams")
            return str("Competition at " + self._location + " with " + str(len(competing)) + " teams")
        else:
            return str(
                # "Competition at " + self._location + " on " + self.date_time + " with " + ",".join(competing)
                # + " teams")
                "Competition at " + self._location + " on " + str(self.date_time) + " with " + str(len(competing)) +
                " teams")


class Emailer:
    _sole_instance = None
    sender_address = None

    @classmethod
    def instance(cls):
        if cls._sole_instance is None:
            cls._sole_instance = cls()
        return cls._sole_instance

    @classmethod
    def configure(cls, prop):
        cls.sender_address = prop

    # send_plain_email(recipients, subject, message) -- Note: this is an instance method.
    def send_plain_email(self, recipients, subject, message):
        for recipient in recipients:
            print(f"Sending mail to: " + recipient)


class DuplicateOid:
    def __init__(self, oid):
        super().__init__(oid)


class DuplicateEmail:
    def __init__(self, email):
        self.email = email


class LeagueDatabase:
    leagues = []
    _sole_instance = None
    _last_oid = 0

    @classmethod
    def instance(cls):
        if cls._sole_instance == None:
            cls._sole_instance = cls
        return cls._sole_instance

    @classmethod
    def last_oid(cls):
        return cls._last_oid

    @classmethod
    def load(cls, load_filename):
        try:
            with open(load_filename, mode='rb') as f:
                cls.leagues = pickle.load(f)
        except FileNotFoundError as e:
            e.strerror = 'File not found, loading backup...'
            try:
                with open(load_filename + 'backup', mode='rb') as j:
                    cls.leagues = pickle.load(j)
            except FileNotFoundError as e:
                e.strerror = 'Backup file not found'




        '''
        try:
            with open(load_filename, mode='rb') as f:
                pickle.load(f)
        except FileNotFoundError as e:
            e.strerror = 'ugh, sorry, it would be better to use the logging framework here but I dont want to go into it'
            raise e
        '''
    def league(self):
        return self.leagues

    def add_league(self, leaguename):
        number = None
        self.leagues.append(leaguename)
        for league in self.leagues:
            number = league.oid
        LeagueDatabase._last_oid = number

    def next_oid(self):
        # LeagueDatabase._last_oid = LeagueDatabase._last_oid + 1
        LeagueDatabase._last_oid = LeagueDatabase._last_oid + 1
        return LeagueDatabase._last_oid

    def save(self, file_name):

        if os.path.isfile(file_name):
            os.rename(file_name, file_name + 'backup')
        try:
            with open(file_name, mode='wb') as f:
                pickle.dump(self.leagues, f)
                f.close()
        except:
            pass

    def import_league(self, league_name, file_name):
        temp_team_name = []

        self.leagues.append(league_name)
        with open(file_name, 'r', encoding='utf-8') as f:
            filereader = csv.reader(f)
            next(filereader)
            for line in filereader:

                c = Team(self.next_oid(), line[0])
                if not (league_name.teams):
                    temp_team_name.append(c)
                    league_name.add_teams(c)
                    d = TeamMember(self.next_oid(), line[1], line[2])
                    c.add_member(d)
                else:
                    #for league in self.leagues:
                        #for teams in league.teams:
                    if c not in temp_team_name:
                        league_name.add_teams(c)
                        temp_team_name.append(c)
                        d = TeamMember(self.next_oid(), line[1], line[2])
                        c.add_member(d)
                    else:
                        pass

                '''
                if line[0] not in league.teams.name:
                League.add_teams(self.next_oid(), line[0])
                if line[0] in league.teams.name:
                pass
                

    def export_league(self,league,file_name):
        try:
            pass

            #with open(file_name,w) as csvfile:
                #print('Waqas')
                #file_writer = csv.writer(f,delimiter=' ')
                #file_writer.writerows(self.leagues)
        except:
            pass

        '''


if __name__ == '__main__':
    # League1 = League(1, 'Cricket League')
    '''
    TeamMember1 = TeamMember(1, 'A', 'A@gmail.com')
    TeamMember2 = TeamMember(2,'B','B@gmail.com')
    Team1 = Team(2, 'A-TEAM')
    Team2 = Team(3, 'B-TEAM')
    Team1.add_member(TeamMember1)
    Team1.add_member(TeamMember2)

    League1 = League(1,'Cricket League')
    League1.add_teams(Team1)
    League1.add_teams(Team2)
    Competition1 = Competition(1, [Team1, Team2], None, None)
    Competition2 = Competition(1, [Team2, Team1], None, None)
    League1.add_competition(Competition1)
    League1.add_competition(Competition2)
    print(League1.teams_for_member(TeamMember1))
    #League1.competitions_for_team(Team1)
    #print(League1.competitions_for_member(TeamMember1))
    #Team1.remove_member(TeamMember1)
    #print(Team1)
    '''
    # League1 = League(1, 'Cricket League')
    L1 = LeagueDatabase()
    # L1.add_league(League1)
    # League1.add_teams(Team1)
    print(L1.last_oid())
    print(L1.next_oid())
    # L1.save("RRRRR.txt")
    # L1.load("RRRRR.txt")
    League1 = League(9, 'Cricket League')
    L1.import_league(League1, "Teams.csv")
    #L1.save('Waqas999')
    #L1.load('Waqas999')
    L1.export_league('Cricket League','Waqas998')




