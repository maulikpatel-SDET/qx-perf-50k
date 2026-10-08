"""Service module 15064: business logic, no crypto."""


def calculate_total_15064(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15064():
    return 'module 15064 handles orders and invoices'
