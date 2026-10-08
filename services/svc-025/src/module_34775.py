"""Service module 34775: business logic, no crypto."""


def calculate_total_34775(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34775():
    return 'module 34775 handles orders and invoices'
