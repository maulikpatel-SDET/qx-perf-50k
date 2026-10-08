"""Service module 21064: business logic, no crypto."""


def calculate_total_21064(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21064():
    return 'module 21064 handles orders and invoices'
