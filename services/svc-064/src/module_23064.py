"""Service module 23064: business logic, no crypto."""


def calculate_total_23064(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23064():
    return 'module 23064 handles orders and invoices'
