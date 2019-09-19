# Consume a REST API

This project is meant to examine your ability to call 3rd party data services
and handle the response from these services.

## Project

Your task is to build and deliver a command line tool with the following requirements:

- [ ] An executable Python file that accepts the required arguments `aggregation`, `field` and `by`, with the range of acceptable values for each described below.
- [ ] Requests `https://dev-interview-countries.leaflink.com/` for data.
- [ ] Outputs aggregated 3rd party data to the console
- [ ] Has reasonable test coverage

### Aggregations

The command line tool should have three required arguments, `aggregation`, `field` and `by`.

`by` values:
  - region
  - subregion

`aggregation` values:

- average
  - acceptable `field` values are:
    - area
    - borders
    - currencies
    - gini
    - languages
    - latitude
    - longitude
    - population
- count
  - acceptable `field` values are:
    - borders
    - countries
    - currencies
    - languages
- max
  - acceptable `field` values are:
    - area
    - gini
    - population
- min
  - acceptable `field` values are:
    - area
    - borders
    - currencies
    - gini
    - languages
    - population
- sum
  - acceptable `field` values are:
    - area
    - gini
    - population


## Examples

### Max area by region

Console input:

`$ get_country_data --aggregation=max --field=area --by=region`

Console output:

```json
{
  "Africa": 2381741,
  "Americas": 9984670,
  "Asia": 9640011,
  "Europe": 17124442,
  "Oceania": 7692024,
  "Polar": 14000000,
  "null": 412
}
```

### Average Languages per Country by subregion

Console input:

`$ get_country_data --aggregation=avg --field=languages --by=subregion`

Console output:

```json
{
  "Australia and New Zealand": 1.2,
  "Caribbean": 1.29,
  "Central America": 1.12,
  "Central Asia": 2.0,
  "Eastern Africa": 1.8,
  "Eastern Asia": 1.25,
  "Eastern Europe": 1.27,
  "Melanesia": 2.0,
  "Micronesia": 1.71,
  "Middle Africa": 1.9,
  "Northern Africa": 1.14,
  "Northern America": 1.17,
  "Northern Europe": 1.44,
  "Polynesia": 1.3,
  "South America": 1.27,
  "South-Eastern Asia": 1.27,
  "Southern Africa": 3.17,
  "Southern Asia": 1.56,
  "Southern Europe": 1.65,
  "Western Africa": 1.12,
  "Western Asia": 1.24,
  "Western Europe": 1.67,
  "null": 2.0
}
```

### Count currencies by region

Console input:

`$ get_country_data --aggregation=count --field=currencies --by=region`

Console output:

```json
{
  "Africa": 49,
  "Americas": 39,
  "Asia": 50,
  "Europe": 26,
  "Oceania": 14,
  "Polar": 2,
  "null": 2
}
```


## Deliverables

- [ ] A new git repo with your project's code.
- [ ] A README file which details how to set up, run and test the project.
- [ ] `--help` output for your command line tool


## Considerations

The endpoint `https://dev-interview-countries.leaflink.com/` is
designed to be unstable, you can expect the response to be delayed
or with other status besides 200 OK; therefore beyond just the
"happy path" of calling a functioning API and parsing a successful
and well-formed response, your solution should also consider various
failure scenarios and handle them gracefully.
