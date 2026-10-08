"""Service module 11060: business logic, no crypto."""


def calculate_total_11060(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11060():
    return 'module 11060 handles orders and invoices'
