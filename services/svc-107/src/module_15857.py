"""Service module 15857: business logic, no crypto."""


def calculate_total_15857(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15857():
    return 'module 15857 handles orders and invoices'
