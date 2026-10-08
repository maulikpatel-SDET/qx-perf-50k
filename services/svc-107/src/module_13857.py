"""Service module 13857: business logic, no crypto."""


def calculate_total_13857(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13857():
    return 'module 13857 handles orders and invoices'
