# Consume a REST API

This project is meant to examine your ability to call 3rd party data services and handle the response from these services.

## Project

Consider the following JSON REST API with a single list endpoint:

```json
http://example.com/api/v1/owners

[
  {
    "owner": {
      "first_name": "tom",
      "last_name": "smith",
      "age": 12
    },
    "pet": "dog"
  }, 
  {
    "owner": {
      "first_name": "lisa",
      "last_name": "wirth",
      "age": 39
    },
    "pet": "bird"
  },
  {
    "owner": {
      "first_name": "marry",
      "last_name": "ann",
      "age": 76
    },
    "pet": "cat"
  },
  {
    "owner": {
      "first_name": "mike",
      "last_name": "ray",
      "age": null
    },
    "pet": "dog"
  }
]
```

Given the above information, your task is to build and deliver a library to consume this API, with the following specifications and requirements:
- [ ] A new git repo with your project's code base.
- [ ] A runnable Python project that consumes the API and outputs information about each owner, grouped by pet
- [ ] Data modeling that reflects the above objects and relationships
- [ ] Reasonable test coverage

## Deliverables

- [ ] A link to a Git repository containing your work.
- [ ] A README file which details how to run the library

## Considerations

Beyond just the "happy path" of calling a functioning API and parsing a successful and well-formed response, your solution should also consider the following exigencies:

- Network Errors
- Timeouts and retries
- Error responses
- Malformed responses (unparseable JSON or an unexpected data structure)

