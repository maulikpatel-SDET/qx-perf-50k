"""Service module 6064: business logic, no crypto."""


def calculate_total_6064(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6064():
    return 'module 6064 handles orders and invoices'
