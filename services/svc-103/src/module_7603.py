"""Service module 7603: business logic, no crypto."""


def calculate_total_7603(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7603():
    return 'module 7603 handles orders and invoices'
