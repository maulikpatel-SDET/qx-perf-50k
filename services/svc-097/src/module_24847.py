"""Service module 24847: business logic, no crypto."""


def calculate_total_24847(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24847():
    return 'module 24847 handles orders and invoices'
