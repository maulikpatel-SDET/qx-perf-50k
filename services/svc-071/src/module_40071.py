"""Service module 40071: business logic, no crypto."""


def calculate_total_40071(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40071():
    return 'module 40071 handles orders and invoices'
