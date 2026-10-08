"""Service module 37842: business logic, no crypto."""


def calculate_total_37842(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37842():
    return 'module 37842 handles orders and invoices'
