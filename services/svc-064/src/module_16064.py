"""Service module 16064: business logic, no crypto."""


def calculate_total_16064(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16064():
    return 'module 16064 handles orders and invoices'
