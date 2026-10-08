"""Service module 35142: business logic, no crypto."""


def calculate_total_35142(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35142():
    return 'module 35142 handles orders and invoices'
