"""Service module 42064: business logic, no crypto."""


def calculate_total_42064(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42064():
    return 'module 42064 handles orders and invoices'
