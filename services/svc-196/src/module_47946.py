"""Service module 47946: business logic, no crypto."""


def calculate_total_47946(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47946():
    return 'module 47946 handles orders and invoices'
