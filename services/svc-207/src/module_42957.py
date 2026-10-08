"""Service module 42957: business logic, no crypto."""


def calculate_total_42957(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42957():
    return 'module 42957 handles orders and invoices'
