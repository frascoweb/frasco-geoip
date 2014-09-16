# Frasco-Geoip

Uses [pygeoip](https://pypi.python.org/pypi/pygeoip) and [Maxmind's databases](http://dev.maxmind.com/geoip/geoip2/geolite2/)
to geolocate the current visitor. Provides command to download the databases.
The session is used as a cache.

## Installation

    pip install frasco-geoip

## Setup

Feature name: geoip

Options:

 - *auto_geolocate*: whether to geolocate the visitor before every requests (default: True)
 - *country_db*: filename of the country database (default: GeoIP.dat)
 - *city_db*: filename of the city database (default: GeoLiteCity.dat)

## Downloading the databases

You will need to download Maxmind's GeoLite databases to be able to
use this feature. They are free and available from <http://dev.maxmind.com/geoip/geoip2/geolite2/>.

This feature provides a command to easily download them:

    $ frasco geoip dlcountries # downloads the country database
    $ frasco geoip dlcities # downloads the city database

## Actions

### geolocate\_country

Geolocates the country of the current visitor using the remote\_addr of the request.

Options:

 - *addr* (default): the ip to geolocate (optional, default is the request's remote\_addr)

Returns the country code.  
Default variable assignment: `$geo_country_code`

### geolocate\_city

Geolocates the city of the current visitor using the remote\_addr of the request.

Options:

 - *addr* (default): the ip to geolocate (optional, default is the request's remote\_addr)

Returns the city record.  
Default variable assignment: `$geo_city`

### clear\_geo\_cache

Clears the cached values in the session

## Debugging

To make things easier, in debug mode the ip address of the visitor can be overrided using
the *__geoaddr* query parameter.