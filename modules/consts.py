import os

VERSION = 1.0
SPLASH_WELCOME = f"Welcome to PyPass {VERSION}! An interactive password manager."
SPLASH_COPYRIGHT = "Copyright 2021 Youngwoo Kim."
SPLASH_TIP = "Enter 'help' to see the list of available commands."

# USER PROMPTS
PROMPT_CMD=">> "
PROMPT_VALUE="> "
PROMPT_MASTER_PW = "Enter master password: "
PROMPT_CURRENT_MASTER_PW = "Enter old master password: "
PROMPT_NEW_MASTER_PW = "Enter new master password: "
PROMPT_CONFIRM_PW = "Re-enter password: "
PROMPT_MASTER_USERNAME = "Enter username: "

PROMPT_NEW_ENTRY_TITLE = "===== Adding new credential entry =====\n"
PROPMT_NEW_ENTRY_NAME = "[1/3] Enter service/domain name: "
PROPMT_NEW_ENTRY_ID = "[2/3] Enter your user ID/email (leave blank if there is none): "
PROMPT_NEW_ENTRY_EMPTY_ID_CONFIRM = "You have not entered anything. Are you sure (y/n)? "
PROMPT_NEW_ENTRY_PASSWORD_1 = "[3/3] Password\n"
PROMPT_NEW_ENTRY_PASSWORD_2 = """<Options>
1. Generate new secure password (recommended)
2. Enter a pasword yourself\n
Choose option (Enter 1 or 2): """
PROMPT_NEW_ENTRY_PASSWORD_USER = "Enter a password for this service: "
PROMPT_NEW_ENTRY_CONFIRM_ENTRY = """The following entry will be created.
Please confirm your input.

================ NEW ENTRY ================
* service/domain name: {}
* ID: {}
* Password: {}
===========================================

Is the information above correct (y/n)? """

PROMPT_SEARCH_QUERY = "Search database by service name: "

PROMPT_EDIT_CHOOSE_ONE = "Enter the entry ID of the item to edit: "
TIP_KEEP_ORIGINAL = " (Leave it blank to keep original)"
PROMPT_EDIT_ENTRY_NAME = "[1/3] Edit service name" + TIP_KEEP_ORIGINAL
PROMPT_EDIT_ENTRY_ID = "[2/3] Edit ID" + TIP_KEEP_ORIGINAL
PROMPT_EDIT_ENTRY_PW = "[3/3] Edit password" + TIP_KEEP_ORIGINAL
PROMPT_EDIT_ENTRY_PW_CONFIRM = "Enter same value again to confirm, leave blank to try again."
PROMPT_EDIT_CONFIRM_CHANGE_1 = "CONFIRM CHANGE"
PROMPT_EDIT_CONFIRM_CHANGE_2 = "{} >> {}"
PROMPT_EDIT_CONFIRM_CHANGE_3 = "Confirm (y/n) ? "
PROMPT_EDIT_IN_PROGRESS = "Saving changes... "

PROMPT_DELETE_CONFIRM = "Are you sure you want to delete the above entry (y/n)? "
PROMPT_DELETE_CONFIRM_2 = "This action cannot be undone. Are you sure (y/n)? "

# RESPONSE MESSAGES
WELCOME_USER = "Welcome, {}"
VIEW_SEARCH_RESULT = "Found {} entries for search '{}'."
EDIT_NO_CHANGES = "No changes. Keep original value: '{}'."

# SUCCESS MESSAGES
SUCCESS_NEW_MASTER_PW = "New master password successfully set."
SUCCESS_EDIT = "All changes saved successfully."
SUCCESS_DELETE = "Deleted credential entry from the database."

# ERROR MESSAGES
ERROR_INIT_MISSING_SALT = 'Cannot unlock database due to missing key file. Stopping...'

ERROR_MODULES_NOT_FOUND = "Dependencies not found. Please install dependencies with \
'python3 -m pip install -r requirements.txt' and try again."

ERROR_PW_CONFIRM = "Passwords do not match. Please try again."
ERROR_PW_TOO_SHORT = "A password needs to be at least {} characters long. Please try again."
ERROR_PW_UNSUPPORTED_CHARS = "Your password contains unsupported character(s). Please try again."
ERROR_PW_EXCEED_MAX_ATTEMPTS = "You got the password wrong too many times. Exiting..."
ERROR_MASTER_PW_WRONG = "Incorrect master password."

ERROR_MASTER_USERNAME_EMPTY = "A username cannot be empty."
ERROR_MASTER_USERNAME_TOO_SHORT = "A username must be at least 3 characters long."
ERROR_MASTER_USERNAME_UNSUPPORTED_CHARS = "Your username contains unsupported character(s). Please try again."

ERROR_NEW_ENTRY_NAME_EMPTY = "You must enter a non-empty service/domain name."
ERROR_NEW_ENTRY_NAME_TOO_LONG = "A service/domain name must be shorter than 512 characters. Please try again."
ERROR_NEW_ID_TOO_LONG = "A user ID/email must be shorter than {} characters. Please try again."
ERROR_NEW_ENTRY_ALREADY_EXISTS = "You already have an entry for the service '{}' in the database."
ERROR_NEW_ENTRY_PW_INVALID_OPTIONS = "Enter either 1 or 2 to select an option. Please try again."
ERROR_NEW_ENTRY_PW_EMPTY = "A password field cannot be left empty. Please try again."

ERROR_VIEW_QUERY_TOO_SHORT = "Search query is too short. Search with at least {} characters as your search query."
ERROR_VIEW_QUERY_TOO_LONG = "Search query is too long. Search with less than {} characters as your search query."
ERROR_VIEW_NO_SEARCH_RESULTS = "No credentials were found for search '{}'."

ERROR_EDIT_ENTRY_ID_NOT_NUMBER = "Enter a valid entry ID. An entry ID is a number. Please try again."

ERROR_DELETE_NOT_INIT = "Failed to access the database. Forgot to decrypt?"
ERROR_DELETE_FAILED = "Failed to delete credential from database."

ERROR_YN_RESPONSE_INVALID = "Error: Invalid response. Enter either 'y' or 'n' as a reponse. Please try again."

ERROR_USER_ABORT = "Command execution was cancelled by user. Aborting..."


# TIPS
SHOW_PW_FLAG = "(Use the '-p' or '--show-password' flag to view your password)"

# PATHS TO DIRECTORIES, FILES
PATH_DATADIR = 'data'

NAME_KEYFILE = 'master.key'
NAME_SALTFILE = 'master.salt'
NAME_DBFILE = 'credentials.db'
NAME_DBFILE_ENC = 'credentials.db.enc'
NAME_MASTER_USERNAMEFILE = 'uname'
NAME_MASTER_USERNAMEFILE_ENC = 'uname.enc'

PATH_KEYFILE = os.path.join(PATH_DATADIR, NAME_KEYFILE)
PATH_SALTFILE = os.path.join(PATH_DATADIR, NAME_SALTFILE)
PATH_DBFILE = os.path.join(PATH_DATADIR, NAME_DBFILE)
PATH_DBFILE_ENC = os.path.join(PATH_DATADIR, NAME_DBFILE_ENC)
PATH_MASTER_USERNAMEFILE = os.path.join(PATH_DATADIR, NAME_MASTER_USERNAMEFILE)
PATH_MASTER_USERNAMEFILE_ENC = os.path.join(PATH_DATADIR, NAME_MASTER_USERNAMEFILE_ENC)

# PARAMETERS
SCRYPT_R = 8
SCRYPT_N = 2 ** 15
SCRYPT_P = 1
SCRYPT_MAX_MEM = 64 * 2 ** 20
SCRYPT_DKLEN = 32

MASTER_PW_MAX_ATTEMPTS = 5
MASTER_PW_MIN_LEN = 6
MASTER_USERNAME_MIN_LEN = 3

SERVICE_NAME_MAX_LEN = 512
USER_ID_MAX_LEN = 512
USER_PW_MIN_LEN = 6

SEARCH_QUERY_MIN_LEN = 3
SEARCH_QUERY_MAX_LEN = 512

# COMMANDS (and their aliases)
CMD_NEW = ['new', 'n']
CMD_VIEW = ['view', 'v', 'find']
CMD_EDIT = ['edit', 'update', 'e']
CMD_DEL = ['delete', 'del', 'd', 'remove']
CMD_LS = ['list', 'ls']
CMD_LOCK = ['lock']
CMD_EXIT = ['exit', 'quit']
CMD_PASSWD = ['passwd'] # change master password

FLAG_SHOW_PW = ['-p', '--show-password']
FLAG_ALL = ['-a', '--all']

# RESPONSES (Answer to y/n prompts)
RESPONSE_YES = ['yes', 'y']
RESPONSE_NO = ['no', 'n']

# MISC
PRINTABLE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ\
    abcdefghijklmnopqrstuvwxyz0123456789\
        !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

QUOTATION_MARK = ['\'', '"']