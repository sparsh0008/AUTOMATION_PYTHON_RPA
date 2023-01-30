Datetime -> year, month, day, hour, minutes, seconds, microseconds, trinfo
            |_____________|    |_____________________________|       |__|
                 DATE                        TIME                   TIMEZONE

date    -> DATE MONTH YEAR
time      -> HOURS MINUTES SECONDS
timedelta

ctime()   -> time modules -> current time
now       -> datetime of datetime modules
today()   -> datetime of datetime module

strftime() - Module
%a		- Sun, Mon
%A 		- Sunday, Monday
%w 	- 0(Sunday),1,2,3,4,5,6(Saturday)
%d 		- 01,02,03 ....... 31
%b 		- Jan, Feb, Mar ....... Dec
%B 		- January, February..........December
%m 	- 01,02,03......12
.
.
.
.
many more