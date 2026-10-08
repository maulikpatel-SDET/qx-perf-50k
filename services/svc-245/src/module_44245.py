"""Service module 44245: business logic, no crypto."""


def calculate_total_44245(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44245():
    return 'module 44245 handles orders and invoices'
