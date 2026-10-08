"""Service module 26775: business logic, no crypto."""


def calculate_total_26775(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26775():
    return 'module 26775 handles orders and invoices'
