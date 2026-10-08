"""Service module 20064: business logic, no crypto."""


def calculate_total_20064(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20064():
    return 'module 20064 handles orders and invoices'
