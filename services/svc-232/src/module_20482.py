"""Service module 20482: business logic, no crypto."""


def calculate_total_20482(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20482():
    return 'module 20482 handles orders and invoices'
