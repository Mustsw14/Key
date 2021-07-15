class LeagueDataBase:
    _sole_instance = None

    @classmethod
    def instance(cls):
        if cls._sole_instance is None:
            cls._sole_instance = cls()
        return cls._sole_instance

    @classmethod
    def load(cls):
        if cls._sole_instance is None:
            cls._sole_instance = cls()
        return cls._sole_instance

"""

Create a class named LeagueDatabase with the following variables and methods.  Note that the load/save functionality can be implemented any way you like but I recommend using the pickle module.

LeagueDatabase -- a singleton

class variable _sole_instance
class method instance() -- returns the sole instance of this database, creating one if it doesn't exist yet
class method load(file_name) -- loads a LeagueDatabase from the specified file and stores it in _sole_instance.  If file_name does not exist or an error occurs when reading it, display a console message (ugh, sorry, it would be better to use the logging framework here but I don't want to go into it) and load the file from the backup (if it exists).  See save() for information on the backup file.

leagues [r/o prop] -- list of the leagues being managed
_last_oid -- private variable holding the last id number that was supplied (see methods below)

add_league(league) -- add the specified league to the leagues list
next_oid() -- increment _last_id and return its new value (used to generate oid's for your objects)
save(file_name) -- save this database on the specified file.  Before saving, check if the file exists and if it does, rename it to file_name with ".backup" added.
import_league(league_name, file_name) -- load a league from a CSV formatted file. (The Python standard library has a nice CSV module (Links to an external site.)).  The file will contain three columns: team name, team member name, email.  The first line of the file will be a "header" line and should be ignored.  The file will be UTF-8 encoded and may contain non-ASCII text.  Add this loaded league to the list of leagues.  If an error occurs while loading a league, display a message on the console.  Here is a sample file. download
export_league(league, file_name) -- write the specified league to a CSV formatted file.  The first line of the file must be a "header" row containing the following text (without the leading spaces):
      Team name, Member name, Member email
If an error occurs while writing a league, display a message on the console.
"""