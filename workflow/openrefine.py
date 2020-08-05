'''
@begin CleanWithOpenRefine @desc OpenRefine Workflow for farmersmarkets dataset
@in farmersmarkets_csv @uri file://data/farmersmarkets.csv

    @begin LoadToOpenRefine @desc Upload farmersmarkets.csv data to OpenRefine
    @in farmersmarkets_csv @uri file://data/farmersmarkets.cv
    @out spreadsheet
    @end CleanWithOpenRefine

    @begin ColumnsToClean @desc Columns that are cleaned
    @in spreadsheet
    @out MarketName
    @out Facebook
    @out Twitter
    @out Website
    @out Youtube
    @out OtherMeida
    @out street
    @out city
    @out x
    @out y
    @out Season1Date
    @out zip
    @out updatedTime
    @end ColumnsToClean

    @begin TrimSpaces @desc Trim leading and trailing white space
    @in MarketName
    @in Facebook
    @in Twitter
    @in Website
    @in Youtube
    @in OtherMeida
    @in street
    @in city
    @in Season1Date
    @in x
    @in y
#    out Facebook_
    @out Twitter_
    @out Youtube_
#    out Season1Date_
    @end TrimSpaces

    @begin CollapseSpaces @desc Collapse consecutive white spaces
    @in MarketName
    @in Facebook
    @in OtherMeida
    @in street
    @in city
    @in Season1Date
    @out MarketName_
    @out city_
    @out Facebook_
    @out Season1Date_
    @end CollapseSpaces

    @begin FormatTime @desc Change 'Month DD YYYY' to 'MM/DD/YYYY'
    @in updatedTime
    @end FormatTime

    @begin ClusterValues @desc Cluster Similar values
    @in MarketName_
    @in city_
    @end ClusterValues

    @begin DeleteNAorNONE @desc Delete na or none values
    @in Facebook_
    @in Twitter_
    @in Youtube_
    @end DeleteNAorNONE

    @begin SplitInto2Columns @desc Split date into Start Date and End Date
    @in Season1Date_
    @out Season1StartDate
    @out Season1EndDate
    @end SPlitInto2Columns

    @begin CleanFormatZip @desc Clean any string and reformat to NNNNN or NNNNN-NNNN
    @in zip
    @end CleanFormatZip

    @begin ToDateType @desc Change data type to date
    @in Season1StartDate
    @in Season1EndDate
    @end ToDateType

@out farmersmarkets-or_csv @uri file://data/farmersmarkets-or.csv
@end CleanWithOpenRefine

'''
