"""Service module 35767: business logic, no crypto."""


def calculate_total_35767(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35767():
    return 'module 35767 handles orders and invoices'
