"""Service module 42479: business logic, no crypto."""


def calculate_total_42479(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42479():
    return 'module 42479 handles orders and invoices'
