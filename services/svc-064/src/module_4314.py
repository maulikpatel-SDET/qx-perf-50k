"""Service module 4314: business logic, no crypto."""


def calculate_total_4314(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4314():
    return 'module 4314 handles orders and invoices'
