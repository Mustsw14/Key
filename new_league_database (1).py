import csv
from csv import reader
import os.path
from os import path

class LeagueDatabase:
    _sole_instance = None
    _leagues = {}

    
    @staticmethod
    def instance(cls):
        if cls._sole_instance is None:
            cls._sole_instance = cls()
        return cls._sole_instance


    def __init__(self):
        if(self._sole_instance): return
        self._sole_instance = True


    def next_oid(self):
        # if index in equal to count
        # then raise StopIteration
        _last_oid += 1
        return _last_oid


    def load(self, file_name):
        #if path.isfile(file_name):
        if path.exists(file_name):
            pass
        elif path.exists(file_name + ".backup"):
            file_name = file_name + ".backup"
            pass
        try:
            with open(file_name, 'r', encoding='utf-8') as csvfile:
                # pass the file object to reader() to get the reader object
                reader = csv.reader(csvfile)
                # headers = next(reader) 
                reader.__next__() # skip first row

                for row in reader:
                    if row[0] not in LeagueDatabase._leagues:
                        LeagueDatabase._leagues[row[0]] = []
                        LeagueDatabase._leagues[row[0]].append([row[1],row[2], row[3]])
                    else:
                        LeagueDatabase._leagues[row[0]].append([row[1],row[2], row[3]])
        except IOError as error:
            print("File does not exists")
        except Exception as ex:
            print("Something went wrong while reading csv")


    @property
    def _last_oid(self):
        return self._last_oid


    @property
    def leagues(self):
        return self._leagues


    def add_league(self,league):
        self._leagues.append(league)


    def save(self,file_name):
        if path.exists(file_name):
            os.rename(file_name, file_name + ".backup") 
            
        # opening the csv file in 'w+' mode
        file = open(file_name, 'w+', newline ='', encoding='utf-8')

        export_list = [] 
        export_list = [["league name","Team name", "Member name", "Member email"]]

        for team in self.leagues._teams:
            for member in team._members:
                export_list.append([self.leagues.name, team.name, member.name, member.email])
        
        # writing the data into the file
        with file:    
            write = csv.writer(file)
            write.writerows(export_list)


    def import_league(self, league_name, file_name):
        #if path.exists(file_name):
            #pass
        #elif path.exists(file_name + ".backup"):
            #file_name = file_name + ".backup"
            #pass
        try:
            with open(file_name, 'r', encoding='utf-8') as csvfile:
                # pass the file object to reader() to get the reader object
                reader = csv.reader(csvfile)
                # headers = next(reader) 
                reader.__next__() # skip first row
                for row in reader:
                    if (row[0],row[1],row[2]) not in LeagueDatabase._leagues[league_name]:
                        LeagueDatabase._leagues[league_name].append([row[0],row[1], row[2]])
                
                #print ("hi")
        except IOError as error:
            print("File does not exists")
        except Exception as ex:
            print("Something went wrong while reading csv")
      


    def export_league(self, league, file_name):
        if path.exists(file_name):
            pass
        elif path.exists(file_name + ".backup"):
            file_name = file_name + ".backup"
            pass

        export_list = [] 
        export_list = [["Team name", "Member name", "Member email"]]
        try:

            for row in LeagueDatabase._leagues[league]:
                export_list.append(row)

            # opening the csv file in 'w+' mode
            file = open(file_name, 'w+', newline ='', encoding='utf-8')

            # writing the data into the file
            with file:    
                write = csv.writer(file)
                write.writerows(export_list)
        except IOError as error:
            print("File does not exists")
        except Exception as ex:
            print("Something went wrong while reading csv")


if __name__ == "__main__":
    obj = LeagueDatabase()
    print("Printing Object")

    #obj.load("leagueTeams.csv")

    obj.import_league( "sunday_League","Teams.csv")

    league = ("sunday_League")
    obj.export_league(league,"Teams.csv")
   

