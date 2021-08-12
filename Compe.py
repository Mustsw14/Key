from abc import ABC, abstractmethod
from league_database import LeagueDatabase


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
         return hash(self._oid)


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
        print("Hi")
        return self._name


    @name.setter
    def name(self,prop):
        if prop is not None:
            self._name = prop

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, prop):
        if email is not None:
            self._email = prop

    def __str__(self):
        return str(self.name + " <" + self.email + ">")

    def __eq__(self, other):
        if hasattr(other, "oid"):
            return self.oid == other.oid
        else:
            return NotImplemented

    def __hash__(self):
        return hash(self.oid)

    def fake_email(self,subject,message):
        send_plain_email(self._email, subject, message)


class Team(IdentifiedObject):

    def __init__(self,oid, _name):
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


    def add_member(self,member):
        if member not in self._members:
            for tm in self._members:
                if tm.email == member.email:
                    raise DuplicateEmail(tm.email)

            self._members.append(member)
        else:
            raise DuplicateOid(self._oid)
        

    def remove_member(self,member):
        if member in self._members:
            self._members.remove(member)


    def __str__(self):
        return str("Team " + self.name + ": " + str(len(self._members)) + " members")


    def __eq__(self, other):
        if isinstance(other, Team) and hasattr(other,"oid"):
            return self._oid == other.oid
        else:
            return NotImplemented


    def __hash__(self):
        return hash(self.oid)


    def send_email(self, emailer, subject, message):
        team_members_emails = []
        for y in self._members:
            team_members_emails.append(y)

        emailer.send_plain_email(team_members_emails, subject, message)


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


    def add_teams(self,team):
        if team not in self.teams:
            self.teams.append(team)
        else:
            raise DuplicateOid(self._oid)


    def add_competition(self,competition):
        if competition not in self.competition:
            self.competition.append(competition)
        else:
            raise DuplicateOid(self._oid)
        

    def teams_for_member(self, member):
        team_names = []
        for team in self.teams:
            if member in team.members:
                team_names.append(team.name)

        return ",".join(team_names)
   

        #  print([team for team in self.teams if member in team.members])


    def competitions_for_team(self,team):
        return [teams for teams in self.competition if team in competition.teams_competing]


    def competitions_for_member(self, member):
        member_teams = [team for team in self._teams if member in team.members]
        return [competition for competition in self.competitions if
                any(x in member_teams for x in competition.teams_competing)]


    def __eq__(self, other):
        if isinstance(other, League) and hasattr(other,"oid"):
            return self._oid == other.oid
        else:
            return NotImplemented


    def __hash__(self):
        return hash(self._oid)

    def __str__(self):
        return str(self.name + ": " + str(len(self.teams)) +" teams," + str(len(self.competition))) +' competition'


class Competition(IdentifiedObject):

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
        _self.date_time = prop

    def send_email(self, emailer, subject, message):
        team_members_emails = None
        for x in self.teams_competing:
            for y in x.members:
                team_members_emails.append(y)
        emailer.send_plain_email(team_members_emails, subject, message)

    def __hash__(self):
        return hash(self.oid)

    def __eq__(self, other):
        if isinstance(other, Competition) and hasattr(other, "oid"):
            return self.oid == other.oid
        else:
            return NotImplemented

    def __str__(self):
        competing =[]
        for test_case in self.teams_competing:
            competing.append( test_case.name)
        if self.date_time is None:
            return str("Competition at " + self._location + " with " + ",".join(competing) + " teams")
        else:
            return str(
                "Competition at " + self._location + " on " + self.date_time + " with " + ",".join(competing)
                + " teams")


class DuplicateOid(Exception):
    def __init__(self, oid):
        self.oid = oid

    def __str__(self):
        return f"Cannot have duplicate DuplicateOid :- {self.oid}"


class DuplicateEmail(Exception):
    def __init__(self, email):
        self.email = email

    def __str__(self):
        return (f"Member with same email address already exists:- {self.email}")


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

    def __int__(self):
        self.recipients = None
        self.subject = None
        self.message = None

    def send_plain_email(self, recipients, subject, message):
        yag = yagmail.SMTP('Mustsw143', 'Winter2024@')
        for recipient in recipients:
            yag.send(recipient, subject, message)
            # print(f"{subject}  {message}:  + recipient.email")


def main():
    # exception Test for team member adding
    member1 = TeamMember(1,"ABC","abc@abc.com")
    member2 = TeamMember(2,"BBC", "bbc@abc.com")
    
   
    team = Team("1", "Fremont")
    team.add_member(member1)
    team.add_member(member2)

    league = League("1", "sunday_league")
    league.add_teams(team)


    obj = LeagueDatabase()
    obj._leagues = league

    obj.load("save_file.csv")

    obj.save("save_file_1.csv")

    obj.import_league( "sunday_league","newteam.csv")

    league = ("sunday_league")
    obj.export_league(league,"Teams.csv")

    print("Done!")


if __name__ == '__main__':
    
    """
        Main method for uploading data and unitesting file
    """
    main()