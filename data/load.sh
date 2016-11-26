
if [[ $# -eq 0 ]] ; then
    echo "Usage:"
    echo "./load.sh filename.pgsql"
    exit 0
fi

if [ ! -f $1 ]
then
   echo "Usage:"
   echo "./load.sh filename.pgsql"
   exit 0
fi

dbname=${1%.pgsql}
#createdb $
echo "Loading $dbname.pgsql into database $dbname"
createdb ${dbname}_test
psql ${dbname}_test < $1
