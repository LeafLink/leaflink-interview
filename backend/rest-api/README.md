# Consume a REST API

This project is meant to examine your ability to call 3rd party data services
and handle the response from these services.

## Project

Your task is to build and deliver a Python API with the following requirements:

- [ ] Listen to HTTP requests.
- [ ] Has a single endpoint `/aggregated-data/`.
- [ ] Requests `https://dev-interview-countries.leaflink.com/` for data.
- [ ] Outputs aggregated 3rd party data.
- [ ] Has reasonable test coverage


### Agreggations

Based on the request GET parameters the endpoint should handle the following
aggregations, all of them by Region or Subregion:

- [ ] Average
  - [ ] Area
  - [ ] Borders per Country
  - [ ] Currencies per Country
  - [ ] Gini
  - [ ] Languages per Country
  - [ ] Latitude, Longitude
  - [ ] Population
- [ ] Count
  - [ ] Borders
  - [ ] Countries
  - [ ] Currencies
  - [ ] Languages
- [ ] Max
  - [ ] Area
  - [ ] Gini
  - [ ] Population
- [ ] Min
  - [ ] Area
  - [ ] Borders per Country
  - [ ] Currencies per Country
  - [ ] Gini
  - [ ] Languages per Country
  - [ ] Population
- [ ] Sum
  - [ ] Area
  - [ ] Gini
  - [ ] Population


## Examples

### Max area by region

`GET /aggregated-data/?aggregation=max&field=area&by=region`

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

`GET /aggregated-data/?aggregation=avg&field=languages&by=subregion`

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

`GET /aggregated-data/?aggregation=count&field=currencies&by=region`

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
- [ ] A README file which details how to execute the API.


## Considerations

The endpoint `https://dev-interview-countries.leaflink.com/` is
designed to be unstable, you can expect the response to be delayed
or with other status besides 200 OK; therefore beyond just the
"happy path" of calling a functioning API and parsing a successful
and well-formed response, your solution should also consider various
failure scenarios and handle them gracefully.
