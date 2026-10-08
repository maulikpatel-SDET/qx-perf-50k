"""Service module 23121: business logic, no crypto."""


def calculate_total_23121(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23121():
    return 'module 23121 handles orders and invoices'
