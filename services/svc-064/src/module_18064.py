"""Service module 18064: business logic, no crypto."""


def calculate_total_18064(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18064():
    return 'module 18064 handles orders and invoices'
