"""Service module 30314: business logic, no crypto."""


def calculate_total_30314(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30314():
    return 'module 30314 handles orders and invoices'
