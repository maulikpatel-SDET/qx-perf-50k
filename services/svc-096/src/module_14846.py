"""Service module 14846: business logic, no crypto."""


def calculate_total_14846(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14846():
    return 'module 14846 handles orders and invoices'
