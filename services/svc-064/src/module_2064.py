"""Service module 2064: business logic, no crypto."""


def calculate_total_2064(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2064():
    return 'module 2064 handles orders and invoices'
