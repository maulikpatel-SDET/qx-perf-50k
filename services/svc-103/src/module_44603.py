"""Service module 44603: business logic, no crypto."""


def calculate_total_44603(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44603():
    return 'module 44603 handles orders and invoices'
