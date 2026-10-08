"""Service module 43201: business logic, no crypto."""


def calculate_total_43201(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43201():
    return 'module 43201 handles orders and invoices'
