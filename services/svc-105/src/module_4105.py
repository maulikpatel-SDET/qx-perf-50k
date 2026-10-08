"""Service module 4105: business logic, no crypto."""


def calculate_total_4105(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4105():
    return 'module 4105 handles orders and invoices'
