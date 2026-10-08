"""Service module 7142: business logic, no crypto."""


def calculate_total_7142(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7142():
    return 'module 7142 handles orders and invoices'
