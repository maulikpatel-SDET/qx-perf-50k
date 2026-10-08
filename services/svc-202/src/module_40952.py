"""Service module 40952: business logic, no crypto."""


def calculate_total_40952(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40952():
    return 'module 40952 handles orders and invoices'
