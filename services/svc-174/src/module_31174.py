"""Service module 31174: business logic, no crypto."""


def calculate_total_31174(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31174():
    return 'module 31174 handles orders and invoices'
