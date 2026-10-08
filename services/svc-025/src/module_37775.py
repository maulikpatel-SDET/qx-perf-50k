"""Service module 37775: business logic, no crypto."""


def calculate_total_37775(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37775():
    return 'module 37775 handles orders and invoices'
