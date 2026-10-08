"""Service module 25775: business logic, no crypto."""


def calculate_total_25775(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25775():
    return 'module 25775 handles orders and invoices'
