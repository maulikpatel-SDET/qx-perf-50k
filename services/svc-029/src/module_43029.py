"""Service module 43029: business logic, no crypto."""


def calculate_total_43029(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43029():
    return 'module 43029 handles orders and invoices'
