"""Service module 43227: business logic, no crypto."""


def calculate_total_43227(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43227():
    return 'module 43227 handles orders and invoices'
