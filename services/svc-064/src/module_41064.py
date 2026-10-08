"""Service module 41064: business logic, no crypto."""


def calculate_total_41064(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41064():
    return 'module 41064 handles orders and invoices'
