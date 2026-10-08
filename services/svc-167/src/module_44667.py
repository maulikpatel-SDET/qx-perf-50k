"""Service module 44667: business logic, no crypto."""


def calculate_total_44667(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44667():
    return 'module 44667 handles orders and invoices'
