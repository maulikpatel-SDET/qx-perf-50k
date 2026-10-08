"""Service module 40466: business logic, no crypto."""


def calculate_total_40466(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40466():
    return 'module 40466 handles orders and invoices'
