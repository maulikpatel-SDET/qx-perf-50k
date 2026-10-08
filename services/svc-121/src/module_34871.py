"""Service module 34871: business logic, no crypto."""


def calculate_total_34871(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34871():
    return 'module 34871 handles orders and invoices'
